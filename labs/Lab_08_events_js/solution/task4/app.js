const inputs = document.querySelectorAll("input");
const bkg = document.querySelector(".main__box-right");
const spans = document.querySelectorAll("span");
const colorContainer = document.getElementById("colorContainer");
const generateBtn = document.getElementById("generate__btn");

let red = 0;
let green = 0;
let blue = 0;
const MAX_COLOR_BLOCKS = 15;

colorContainer.addEventListener("click", (event) => {
  const clickedColorBlock = event.target.closest(".color__block");

  if (clickedColorBlock) {
    const clickedColor = getComputedStyle(clickedColorBlock).backgroundColor;
    localStorage.setItem("selectedColor", clickedColor);
  }
});

function updateColor() {
  bkg.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

function createColorBlock() {
  const colorBlock = document.createElement("div");
  colorBlock.classList.add("color__block");
  colorContainer.prepend(colorBlock);
  colorBlock.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;

  const colorBlocks = document.querySelectorAll(".color__block");
  if (colorBlocks.length > MAX_COLOR_BLOCKS) {
    colorContainer.removeChild(colorBlocks[colorBlocks.length - 1]);
  }
}

inputs.forEach((input, index) => {
  input.addEventListener("input", () => {
    const label = input.closest(".box__left-control").querySelector("label");
    const inputValue = +input.value;

    if (inputValue >= 0 && inputValue <= 255) {
      input.style.borderColor = "green";
      switch (label.innerText) {
        case "red":
          red = inputValue;
          break;
        case "green":
          green = inputValue;
          break;
        case "blue":
          blue = inputValue;
          break;
      }
      spans[index].style.visibility = "hidden";
      updateColor();
    } else {
      input.style.borderColor = "red";
      spans[index].style.visibility = "visible";
    }
  });
});

generateBtn.addEventListener("click", createColorBlock);

document.addEventListener("click", (event) => {
  const selectedColor = localStorage.getItem("selectedColor");
  if (selectedColor) {
    const target = event.target;
    if (
      target !== colorContainer &&
      target !== generateBtn &&
      !colorContainer.contains(target) &&
      target !== bkg
    ) {
      target.style.backgroundColor = selectedColor;
    }
  }
});
