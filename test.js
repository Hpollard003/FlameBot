var foo = 101;
function func1() {
    return function() {
        console.log(foo);
    }
    var foo = 202;
}
var func2 = func1()
func2()