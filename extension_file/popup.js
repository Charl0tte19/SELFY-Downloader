

window.onload = function(){
	
	var up = document.getElementById('update');
	up.addEventListener('click',function(){
		var port = chrome.runtime.connectNative('com.my_extension.newest_banner');
		port.onDisconnect.addListener(function () {
			if (chrome.runtime.lastError) {
				console.log(chrome.runtime.lastError);
			}
		});
	});
	
	var newest = document.getElementById('img-new')
	newest.addEventListener('click',function(){
		chrome.tabs.create({url:'https://sp.atgames.jp/pocketland/information/list/index?placeId=38'})
	});
	
	var trade = document.getElementById('trade')
	trade.addEventListener('click',function(){
		chrome.tabs.create({url:'http://li.nu/attrade/gacha.php'})
	});
	
	var notif01 = {
		type: 'basic',
		iconUrl: 'icon/icon48.png',
		title: '警告！',
		message: '該操作在當前頁面無效'
	};
	

	chrome.storage.sync.get(['from_val'],function(btn){
		$("#from").val(btn.from_val);
	})
	
	var from_btn = document.getElementById('f_btn')
	
	$("#from").blur(function(){
		if($("#from").val()!="")
				chrome.storage.sync.set({'from_val':$("#from").val()})
	});
		
	
	from_btn.addEventListener('click',function(){
		chrome.tabs.getSelected(null, function (tab) { 
			if((tab.url).indexOf('http://li.nu/attrade/gachalist.php?gacha=')==-1){
				chrome.notifications.create('page_error',notif01);
				chrome.notifications.clear('page_error')
			}
			else{
				var num = (tab.url).split('=')[1];
				$("#from").val(num);
				chrome.storage.sync.set({'from_val':num})
			}
		});
	});
	
	
	
	chrome.storage.sync.get(['to_val'],function(btn){
		$("#to").val(btn.to_val);
	})

	$("#to").blur(function(){
		if($("#to").val()!="")
				chrome.storage.sync.set({'to_val':$("#to").val()})
	});
	
	var to_btn = document.getElementById('t_btn')
	to_btn.addEventListener('click',function(){
		chrome.tabs.getSelected(null, function (tab) { 
			if((tab.url).indexOf('http://li.nu/attrade/gachalist.php?gacha=')==-1){
				chrome.notifications.create('page_error',notif01);
				chrome.notifications.clear('page_error')
			}
			else{
				var num2 = (tab.url).split('=')[1];
				$("#to").val(num2);
				chrome.storage.sync.set({'to_val':num2})
			}
		});
	});
	
	var d_range = document.getElementById('download_range');
	d_range.addEventListener('click',function(){
		var port = chrome.runtime.connectNative('com.my_extension.send_range');
		port.postMessage({'from':$("#from").val(),'to':$("#to").val()});
		var port2 = chrome.runtime.connectNative('com.my_extension.download_in_range');
		port.onDisconnect.addListener(function () {
			if (chrome.runtime.lastError) {
				console.log(chrome.runtime.lastError);
			}
		});
		port2.onDisconnect.addListener(function () {
			if (chrome.runtime.lastError) {
				console.log(chrome.runtime.lastError);
			}
		});
		

	});
	
	var d_now = document.getElementById('now');
	d_now.addEventListener('click',function(){
		chrome.tabs.getSelected(null, function (tab) { 
			if((tab.url).indexOf('http://li.nu/attrade/gachalist.php?gacha=')==-1){
				chrome.notifications.create('page_error',notif01);
				chrome.notifications.clear('page_error')
			}
			else{
				var num_now = (tab.url).split('=')[1];
				var port = chrome.runtime.connectNative('com.my_extension.send_range');
				port.postMessage({'from': num_now,'to': num_now });
				port.onDisconnect.addListener(function () {
				if (chrome.runtime.lastError) {
					console.log(chrome.runtime.lastError);
				}
				});
				var port2 = chrome.runtime.connectNative('com.my_extension.download_in_range');
				port.onDisconnect.addListener(function () {
				if (chrome.runtime.lastError) {
					console.log(chrome.runtime.lastError);
				}
				});
				port2.onDisconnect.addListener(function () {
				if (chrome.runtime.lastError) {
					console.log(chrome.runtime.lastError);
				}
				});
			}
		});
		
	});
		

	var d_new = document.getElementById('download_new');
	d_new.addEventListener('click',function(){
		var port = chrome.runtime.connectNative('com.my_extension.download_to_newest');
		port.onDisconnect.addListener(function () {
			if (chrome.runtime.lastError) {
				console.log(chrome.runtime.lastError);
			}
		});
		

	});

}