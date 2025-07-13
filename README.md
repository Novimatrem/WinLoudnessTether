# WinLoudnessTether

A Windows, PowerShell version of several of my previous scripts, combined into one.

This script combines my prior warning-sound-if-volume-is-x-percent, limit-audio-max-volume-to-x-percent, & hearing-protector-x-megapack.

# Running

PowerShell scripts are disabled by default on Windows. To enable them, run the following commands in an elevated (Run as Admin) PowerShell terminal, in this exact order:

First

``
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
``

(then type the letter a and press Enter to agree Yes to All)

Second

``
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
``

(then type the letter a and press Enter to agree Yes to All)
