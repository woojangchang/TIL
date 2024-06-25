from openai import OpenAI
from collections import deque
import tiktoken
from IPython.display import Markdown, DisplayHandle

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    "Return the number of tokens used by a list of messages."
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


class Chatbot:
    def __init__(self, api_key, max_history=10, gpt_model='gpt-4o', max_tokens=4096, system_msg="You are an assistant."):
        # OpenAI API client 초기화
        self.client = OpenAI(api_key=api_key)
        self.gpt_model = gpt_model
        self.max_tokens = max_tokens
        # 대화 기록을 기록할 deque 정의
        self.chat_history = deque(maxlen=max_history)
        self.system_msg = [{"role":"system", "content":system_msg}]

        
    def adjust_max_tokens(self):
        messages = self.system_msg + list(self.chat_history)
        num_tokens = num_tokens_from_messages(messages, model=self.gpt_model)

        # 메시지에 이미 있는 토큰 수를 기반으로 max_tokens 조정
        if self.gpt_model == 'gpt-3.5-turbo':
            # max_tokens만큼 확보
            while num_tokens > 4096 - self.max_tokens and self.chat_history:
                self.chat_history.popleft()
                num_tokens = num_tokens_from_messages(self.system_msg + list(self.chat_history), model=self.gpt_model)
        elif self.gpt_model == 'gpt-4':
            while num_tokens > 8192 - self.max_tokens and self.chat_history:
                self.chat_history.popleft()
                num_tokens = num_tokens_from_messages(self.system_msg + list(self.chat_history), model=self.gpt_model)
        elif self.gpt_model in ['gpt-4-turbo', 'gpt-4o']:
            # 전체 토큰 수가 50000개를 넘지 않도록 조정 (요금, 속도를 위해 축소)
            # 필요에 따라 128000개로 조정
            max_tokens = 50000
            while num_tokens > max_tokens and self.chat_history:
                self.chat_history.popleft()
                num_tokens = num_tokens_from_messages(self.system_msg + list(self.chat_history), model=self.gpt_model)
                
                
                
    def ask(self, question):
        # 새로운 질문을 deque에 추가
        self._add_to_history({"role":"user", "content":question})
        self.adjust_max_tokens()  # 토큰 수 조정

        # 시스템 메시지와 이전 대화를 합쳐 prompt 생성
        prompt = self.system_msg + list(self.chat_history)

        dh = DisplayHandle()  # DisplayHandle 인스턴스 생성
        dh.display(Markdown(''))
        
        # API request
        answer = ''
        stream = self.client.chat.completions.create(
            model=self.gpt_model,
            max_tokens=self.max_tokens,
            messages=prompt,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stream=True
        )

        # OpenAI GPT API 호출
        for chunk in stream:
            resp = chunk.choices[0].delta.content
            if resp is not None:
                answer += resp
                dh.update(Markdown(answer))
        
        # 대화 기록 추가
        self._add_to_history({"role":"assistant", "content":answer})
        
        return answer

    def _add_to_history(self, message):
        self.chat_history.append(message)