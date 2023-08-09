<p align="center">
  <img align="center" width="200" src="https://github.com/Alv777/Lightweight_Browser/assets/35309997/2f1d7b5a-5d1d-47b6-9f3f-127548704f5d" />

  <h1 align="center">Photon Browser</h1>
  <h3 align="center">Making the world's fastest, simplest and most efficient browser ever.</h3>
</p>

<!-- Badges -->
<p align="center">
  <a href="https://github.com/Alv777/Lightweight_Browser/issues">
    <img src="https://img.shields.io/github/issues/Alv777/Lightweight_Browser?style=flat-round">
  </a>

  <a href="https://github.com/PiyushSuthar/github-readme-quotes/pulls">
    <img src="https://img.shields.io/github/issues-pr/Alv777/Lightweight_Browser?style=flat-round">
  </a>

  <a href="https://creativecommons.org/licenses/by-nc/4.0/">
    <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg">
  </a>

## Introduction
Photon Browser aims to provide an open-source fast and resource efficient browser with modern design. Using python as it's programming code we can not only achieve using the least ammount of storage, but we can also achieve fast browsing, altough this is limited for the browser engine so the C edition would be a lot faster and will probably use less storage. But for now I'm working on making the best version I can, trying to find the limitations of python and also learning on the way.

(Picture titles may be Light Browser, this was because it was still not decided how to name it.)
### Interface: 
<img width="1024" align="center" src=https://github.com/Alv777/Lightweight_Browser/assets/35309997/9fe8d5ad-1af2-4dad-ad1a-3f09b2464486>

(subject to change)
### Performance:

Photon Browser             |  Google Chrome
:-------------------------:|:-------------------------:
<img width="1100" align="center" src=https://github.com/Alv777/Lightweight_Browser/assets/35309997/803b18cf-d37b-4a00-87dd-9c28e55b4693> |  <img width="1024" align="center" src=https://github.com/Alv777/Lightweight_Browser/assets/35309997/77cc2051-9b7d-49ab-aca3-a075f62aa160>
<img width="650" align="center" src=https://github.com/Alv777/Lightweight_Browser/assets/35309997/7388f8b2-744d-4569-b32a-6f9729ce22a5>| <img width="650" align="center" src=https://github.com/Alv777/Lightweight_Browser/assets/35309997/4ac434b8-1163-4e4b-94c5-639da39362b3>

As you can see, with the same ammount of tabs opened we get less ram usage, about a decrease of -39% which it isnt much but still amazing having in mind we are using the same engine, have to add that photon browser will be optimized and even changed completly in langauge which will decrease ram usage very drastically. This is even the first stable version and has amazed me to be honest.

Trello board: https://trello.com/b/BSmCyDYt
## How to build
#### 1. First you have to install the compiler, make sure you have python and pip installed and then run on a terminal:
```
python -m pip install -U nuitka
```
It may ask you to install a C compiler if you haven't installed any, if prompted type Y and it will be downloaded.

#### 2. After it is done installing you will now proced to clone the repository with:
```
git clone https://github.com/Alv777/Lightweight_Browser.git
```
Also, to run this command you will need to have git installed, and before running make sure you're on the directoy where you want to download it. 
<details>
<summary>Git installation:</summary>

### For windows:
```
https://gitforwindows.org/ 
```
You will need to download it from this website and follow the wizard installation.

### For Linux:
```
sudo apt-get install git-all
```
(Yes in linux is much easier)
### For MacOS:
Go to the following website and download the file:
```
https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect
```
Then follow the instructions of the installer and you will be able to proceed.

### After you're done:
Check if git was correctly installed running on a terminal:
```
git version
```

Source: https://github.com/git-guides/install-git
</details>

#### 3. After cloning we will proceed to compile the program:
Fist open a terminal on the directory of the program or cd into it.
```
cd Lightweight_Browser
```
Then run the compiler and convert it into an exe.
```
python -m nuitka light_browser.py --windows-disable-console
```
When it ends compiling, you will have built the browser and you will be able to use it fully.

#### If you need help or had issues during the installation process either create an issue request or send me an email. 
#### Have fun browsing!
#### Contact: alvarogrp@proton.me
