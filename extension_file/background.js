
chrome.runtime.onMessage.addListener(function(response, sender, sendResponse){
		console.log(response)
		var port = chrome.runtime.connectNative('com.my_extension.send_setting');
		port.postMessage(response);
		port.onDisconnect.addListener(function () {
			if (chrome.runtime.lastError) {
				console.log(chrome.runtime.lastError);
			}
		});
		var notifOptions = {
			type: 'basic',
			iconUrl: 'icon/icon48.png',
			title: '使用者設定',
			message: '更新完成'
		};
		
		chrome.notifications.create('update_finish',notifOptions);
		chrome.notifications.clear('update_finish')
			
});

