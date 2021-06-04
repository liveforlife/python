// a phantomjs example
var page = require('webpage').create()
phantom.outputEncoding = 'gbk'
page.open('http://www.cnblogs.com/front-Thinking', function (status) {
  if (status === 'success') {
    console.log(page.title)
  } else {
    console.log(status, 'reason', page.reason)
  }
  phantom.exit(0)
})

page.onResourceError = function (e) {
  page.reason = e.errorString
}
