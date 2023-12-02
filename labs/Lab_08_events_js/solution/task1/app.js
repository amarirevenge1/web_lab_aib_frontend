const btnFirst = document.getElementById("first_btn");
const btnSecond = document.getElementById("second_btn");
const btnThird = document.getElementById("third_btn");
const background = document.querySelector("body");

function changeBodyBg(color) {
  if (background.style.background === color) {
    background.style.background = "white";
  } else {
    background.style.background = color;
  }
}

btnFirst.onclick = function () {
  changeBodyBg("red");
};

btnSecond.onclick = function () {
  changeBodyBg("green");
};

btnThird.onclick = function () {
  changeBodyBg("blue");
};
