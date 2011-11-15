var http = require('http'); // require Node.js自带的 http 模块
var url = require('url');

// v0.1
/*
http.createServer(function (request, response) {
	response.writeHeader(200, {"Content-Type": "text/plain"});
	response.write("Hello, World!");
	response.end();
}).listen(8888);
*/

// v0.2 将处理请求的函数提取出来
/*
function onRequest(request, response) {
	console.log("Request received.");
	response.writeHeader(200, {"Content-Type": "text/plain"});
	response.write("Hello, World!");
	response.end();
}

http.createServer(onRequest).listen(8888);

console.log("Server has started.");
*/

// 创建成一个模块
function start(route, handle) {
	function onRequest(request, response) {
		var pathname = url.parse(request.url).pathname;
		console.log("Request for " + pathname + " received.");
		route(handle, pathname, response, request);
		
		//console.log("Request received.");
		//response.writeHeader(200, {"Content-Type": "text/plain"});
		//response.write(content);
		//response.end();
		//var postData = "";
		//request.setEncoding("utf8");
		//request.addListener("data", function(postDataChunk) {
		//	postData += postDataChunk;
		//	console.log("Received POST data chunk: " + postDataChunk + ".");
		//});
		//request.addListener("end", function() {
		//	route(handle, pathname, response, postData);
		//});
	}

	http.createServer(onRequest).listen(8888);

	console.log("Server has started.");
}

exports.start = start;
