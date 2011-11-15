function route(handle, pathname, response, postData) {
	console.log("About to route a request for " + pathname);
	
	if (typeof handle[pathname] === 'function') {
		handle[pathname](response, postData);
	} else {
		console.log("No request hndler found for " + pathname);
		response.writeHead(400, {"Content-Type": "text/plain"});
		response.write("<h1>404 Not found</h1>");
		response.end();
	}
}

exports.route = route