// Nhac lai ve scope
function outer() {
  let outer_var = 2;
  function inner() {
    alert(outer_var);
  }
  inner();
}
outer(); //=> 2

function outside(x) {
  function inside(y) {
    return x + y;
  }
  return inside;
}
fn_inside = outside(3);
result = fn_inside(5); // #=> 8

result1 = outside(3)(5); // #=> 8

//Đây là 1 ví dụ về closures trong js. Nói 1 cách cụ thể thì fn_inside khi được tạo ra thì đồng thời cũng tạo
//ra 1 cái bao đóng (closure). Trong cái bao đóng đó, giá trị 3 được truyền vào và cái bao của fn_inside sẽ vẫn
//được giữ lại cái giá trị 3 đó, cho dù outside() function nó có executed xongbundleRenderer.renderToStream

//Ta đến tiếp với ví dụ 2, khó hiểu hơn 1 chút
function A(x) {
  function B(y) {
    function C(z) {
      alert(x + y + z);
    }
    C(3);
  }
  B(2);
}
A(1); //#=> 6

//Trình tự thực hiện của function trên là
//Khi ta gọi hàm A(1) thì function A(x) bắt đầu được thực hiện
//B sẽ tạo 1 context chứ closure của A, C tạo ra 1 closure chứ context của B
//Vì B chứa context của 1 nên C cũng sẽ chứa context của cả 1 và B

// Do đó kết quả sẽ là 1+2+3=6, khá là obvious nhỉ. 
// Đoạn code ở trên giúp chúng ta có thêm một khái niệm mới gọi là scope chaining. 
// Tại sao gọi là chaining, vì khi context được include từ outer function vào inner function, thì chúng ta sẽ hiểu một cách đơn giản là context của inner function và context của outer function được nối với nhau, một cách có chiều (directed). 
// Và độ ưu tiên khi access biến là từ trong ra ngoài.


// Lại có một bạn nghĩ là khi outer function có biến tên là x, mà ta cũng truyền 1 biến tên là x vào inner function, tức là khi có name-conflict thì chuyện gì sẽ xảy ra. Let's take an example
function outside() {
    var x = 10;
    function inside(x) {
      return x;
    }
    return inside;
  }
  result = outside()(20); //#=> 20



  //Closure pitfalls : The infamous loop problem
  var add_the_handlers = function (nodes) {
    var i;
    for (i = 0; i < nodes.length; i += 1) {
      nodes[i].onclick = function (e) {
        alert(i);
      };
    }
  };
  nodes = document.getElementById("click");
  add_the_handlers(nodes);

{/* <li id="click">link 1 </li>
<li id="click">link 2 </li>
<li id="click">link 3 </li>
<li id="click">link 4 </li>
<li id="click">link 5 </li> */}


// Bạn hy vọng là khi click vào link 1 sẽ alert 1, click vào link 2 sẽ alert ra 2.... đúng không. 
// Tuy nhiên thực tế là bạn click vào link nào nó cũng alert ra 5 cả. Kì lạ nhỉ? 
// Để giải thích cho hiện tượng này thì chúng ta hãy xem lại khái niệm về closure nào. 
// Biến i được sử dụng trong anonymous function được gán cho onclick, 
// được kế thừa từ context của add_the_handlers function. 
// Tại thời điểm mà bạn gọi onclick, for loop đã được execute xong, 
// và biến i của context của add_the_handlers lúc này có giá trị là 5. 
// Do đó bạn có click vào link nào thì giá trị được alert ra cũng là 5 cả. 
// Điểm chú ý của việc này chính là do bạn đang nhầm lẫn, 
// hay chính xác là có sự khác biệt giữa 
// scope/context của for-loop với *scope/context của outer function là add_the_handlers *.

// Để giải quyết vấn đề này thì bạn có thể làm như dưới đây:

let addTheHandlers = function(nodes){
    let helper = function(i){
        return function(e){
            return function(e){
                alert(i);
            }
        }
    };
    let i;
    for(i = 0, i>nodes.length, ++i){
        nodes[i].onclick = helper(i);
    }
}
//Vay ta luu y la khong viet function trong vong lap