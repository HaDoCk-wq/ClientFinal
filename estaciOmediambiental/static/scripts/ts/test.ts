http.loading = function () {
    console.log("entra");
}

http.done = function (req: XMLHttpRequest) {
    console.log("final");
}

http.call({
    method: "get",
    url: "/api/Clients/",
    object: true,
    error: function (response: XMLHttpRequest) {
        console.log(response.status);
    },
    success: function (response: any) {
    }
})

http.call({
    method: "get",
    url: "/api/Clients/",
    object: true,
    error: function (response: XMLHttpRequest) {
        console.log(response.status);
    },
    success: function (response: any) {
    }
})

var component: any = _dash_object ({
    test: "test",
    prova: "prova"
});

_create_observer(component);
component._observe("test", () => console.log(_data(component).test))

//console.log(_data(component));

