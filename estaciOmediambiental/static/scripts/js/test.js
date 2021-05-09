http.loading = function () {
    console.log("entra");
};
http.done = function (req) {
    console.log("final");
};
http.call({
    method: "get",
    url: "/api/Clients/",
    object: true,
    error: function (response) {
        console.log(response.status);
    },
    success: function (response) {
    }
});
http.call({
    method: "get",
    url: "/api/Clients/",
    object: true,
    error: function (response) {
        console.log(response.status);
    },
    success: function (response) {
    }
});
var component = _dash_object({
    test: "test",
    prova: "prova"
});
_create_observer(component);
component._observe("test", () => console.log(_data(component).test));
//console.log(_data(component));
