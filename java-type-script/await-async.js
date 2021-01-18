TIMEOUT = 3000
RETURN_VALUE = "I'm done!"

// callback
function callAPIwithCallback(callback) {
    setTimeout(() => {
        callback(RETURN_VALUE)
    }, TIMEOUT)
}

callAPIwithCallback((returnResult) => {
    console.log("Callback returns: ", returnResult)
})

// promise
function callAPIwithPromise() {
    return new Promise(function (resolve, reject) {
        setTimeout(() => {
            resolve(RETURN_VALUE)
        }, TIMEOUT)
    })
}

callAPIwithPromise().then(returnResult => console.log("Promise returns: ", returnResult))

// async-await
// await needs to be in an async function
async function asyncFunction() {
    var returnResult = await callAPIwithPromise()
    console.log("Async-await returns: ", returnResult)
}

asyncFunction()
