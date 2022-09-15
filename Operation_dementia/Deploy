Get-MpComputerStatus
REM #check microsoft defender status


if(Set-MpPreference -DisableBehaviorMonitoring == True) set -disablebehaviormonitoring = false
rem #DISABLE BEHAVIOR MONITORING

if(Set-MpPreference -DisableIOAVProtection == True) set -disableioavprotection = false

rem #DISABLE IOAV PROTECTION
if (AntivirusEnabled == True) Set AntivirusEnabled = False

rem #DISABLE ANTIVIRUS



rem #if defender is enabled, disable it




rem #if defender is disabled, update the 



REM #check if defender is enabled or not


REM #if defender is enabled, start a quick scan
if(MpComputerStatus == True) Start -MpWDOScan -ScanType QuickScan
REM #if defender is disabled, start a full scan

if(MpComputerStatus == False) Start -MpScan -ScanType FullScan



REM #remove t
if(Remove-MpThreat == True) start remove-MpThreathreats






