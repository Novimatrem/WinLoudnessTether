# WinLoudnessTether

A Windows, PowerShell version of several of my previous scripts, combined into one.

This script combines my prior warning-sound-if-volume-is-x-percent, limit-audio-max-volume-to-x-percent, & hearing-protector-x-megapack.

# Running

PowerShell scripts are disabled by default on Windows. To enable them, run the following commands in an elevated (Run as Admin) PowerShell terminal:

``
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
``

``
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
``
