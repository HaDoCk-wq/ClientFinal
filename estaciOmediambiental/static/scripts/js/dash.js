function _id(id) {
    return document.getElementById(id);
}
;
function _select(querry) {
    return document.querySelectorAll(querry);
}
;
function _first(id) {
    return document.querySelector(id);
}
;
function _create(element) {
    var div = document.createElement('div');
    div.innerHTML = element.trim();
    return div.firstChild;
}
;
HTMLElement.prototype._hide = function () {
    this.setAttribute("style", "display: none;");
};
HTMLElement.prototype._show = function () {
    this.removeAttribute("style", "display: unset;");
};
HTMLElement.prototype._delete = function () {
    this.remove();
};
HTMLElement.prototype._apend = function (element) {
    this.appendChild(element);
};
//################################### Reactive engine #######################################
function makeReactive(obj, key) {
    let val = obj[key];
    Object.defineProperty(obj, key, {
        get() {
            return val;
        },
        set(newVal) {
            val = newVal;
            _notify(key);
        }
    });
}
function _create_observer(obj) {
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            makeReactive(obj, key);
        }
    }
}
let signals = {};
function _observe(property, signalHandler) {
    if (!signals[property])
        signals[property] = [];
    signals[property].push(signalHandler);
}
function _notify(signal, newVal) {
    if (!signals[signal] || signals[signal].length < 1)
        return;
    signals[signal].forEach((signalHandler) => signalHandler());
}
function _dash_object(dataObj) {
    let signals = {};
    _create_observer(dataObj);
    return {
        data: dataObj,
        _observe,
        _notify
    };
    function _observe(property, signalHandler) {
        if (!signals[property])
            signals[property] = [];
        signals[property].push(signalHandler);
    }
    function _notify(signal) {
        if (!signals[signal] || signals[signal].length < 1)
            return;
        signals[signal].forEach((signalHandler) => signalHandler());
    }
    function _makeReactive(obj, key) {
        let val = obj[key];
        Object.defineProperty(obj, key, {
            get() {
                return val;
            },
            set(newVal) {
                val = newVal;
                _notify(key);
            }
        });
    }
    function _create_observer(obj) {
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                _makeReactive(obj, key);
            }
        }
    }
}
function _data(_dash_object) {
    return _dash_object.data;
}
