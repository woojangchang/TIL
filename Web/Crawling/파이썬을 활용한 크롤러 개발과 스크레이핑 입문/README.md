# 베이그런트로 윈도우에 우분투 가상 환경 설치하기

macOS와 리눅스를 기반으로 크롤링하는 방법을 위한 가상환경 설치

## 베이그런트 설치하기

가상 환경 구축 방법은 여러 가지가 있지만 베이그런트(vagrant)가 간단하고 깔끔한 편

1. VirtualBox 다운로드 ([링크](https://www.virtualbox.org/wiki/Downloads)) - 운영체제에 맞게 설치
2. 베이그런트 다운로드 ([링크](https://www.vagrantup.com/)) 및 설치

## 베이그런트로 우분투 가상 환경 설치하기

1. 컴퓨터 재부팅 후 명령 프롬프트 실행

2. 우분트 리눅스를 설치할 적당한 디렉터리로 이동 - user 폴더

3. 적당한 이름의 디렉터리를 생성하고 이동

   `C:\Users\user>cd c:\`

   `C:\>mkdir vagrant`

   `C:\>cd vagrant`

4. 우분투 내려받고 설치하기 - 디렉터리에 Vagrantfile 등의 파일이 생성되며 가상 환경이 설정됨

   `C:\vagrant>vagrant init hashicorp/precise64`

## 베이그런트로 우분투 가상 환경 실행하기

리눅스 가상 환경에 들어갈 때 입력하는 명령어이므로 컴퓨터를 종료했다가 다시 실행하면 그때마다 실행해줘야 하는 명령어

1. 가상 환경 실행하기 - 처음 실행한다면 설치까지 진행하여 오래 걸림

   `C:\vagrant>vagrant up`

   - Error가 났을 경우 : BIOS에 접속하여 virtualization을 활성화

2. 접속하기

   `C:\vagrant>vagrant ssh`

```
Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Your Ubuntu release is not supported anymore.
For upgrade information, please visit:
http://www.ubuntu.com/releaseendoflife

New release '14.04.6 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Welcome to your Vagrant-built virtual machine.
Last login: Fri Sep 14 06:23:18 2012 from 10.0.2.2
vagrant@precise64:~$
```

## 파일 공유하기

vagrant는 vagrant 명령어를 실행한 디렉터리를 /vagrant 디렉터리로 공유

1. 공유할 파일을 앞서 생성한 `vagrant` 폴더에 복사(test.py)

2. /vagrant 디렉터리로 이동

   `vagrant@precise64:~$ cd /vagrant`

3. 파일 리스트 확인

   `vagrant@precise64:/vagrant$ ls -l`

