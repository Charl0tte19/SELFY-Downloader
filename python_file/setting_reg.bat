REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_extension.send_range" /t REG_SZ /d "%~dp0json\send_range.json" /f

REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_extension.send_setting" /t REG_SZ /d "%~dp0json\send_setting.json" /f

REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_extension.download_to_newest" /t REG_SZ /d "%~dp0json\download_to_newest.json" /f

REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_extension.download_in_range" /t REG_SZ /d "%~dp0json\download_in_range.json" /f

REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_extension.newest_banner" /t REG_SZ /d "%~dp0json\newest_banner.json" /f