window.onload = init;

const renderServiceContent = (id = 0) => {
  const services = document.querySelectorAll(".service-item");
  services.forEach((element, index) => {
    if (index === id) {
      element.classList.remove("hidden");
      return;
     };
    element.classList.add("hidden");
  });

};

// const scrollToContent = () => {
//   document
//     .getElementById("service-full")
//     .scrollIntoView({ block: "nearest", behavior: "smooth" });
// };

function serviceClick(id) {
  renderServiceContent(id);
  // element.scrollIntoView();
  // scrollToContent();
}

function init() {
  prepareArrowsForScroll();
}

// gallery
const slider = document.querySelector(".gallery");
let isDown = false;
let startX;
let scrollLeft;
if (slider) {
  slider.addEventListener("mousedown", (e) => {
    isDown = true;
    slider.classList.add("active");
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
  });
  slider.addEventListener("mouseleave", (_) => {
    isDown = false;
    slider.classList.remove("active");
  });
  slider.addEventListener("mouseup", (_) => {
    isDown = false;
    slider.classList.remove("active");
  });
  slider.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const SCROLL_SPEED = 3;
    const walk = (x - startX) * SCROLL_SPEED;
    slider.scrollLeft = scrollLeft - walk;
  });
}

prepareArrowsForScroll = () => {
  const buttonRight = document.getElementById("slideRight");
  const buttonLeft = document.getElementById("slideLeft");
  const galleryContainer = document.getElementById("gallery");
  const liGalleryItems = document.getElementsByClassName("gallery-item");
  const serviceButtons = document.getElementsByClassName("services-buttom");


  const serviceButtonsArray = Array.prototype.map.call(serviceButtons, item => item);

  const galleryItemDefaultPadding = window
    .getComputedStyle(buttonRight, null)
    .getPropertyValue("width");

  const arrowsWidth =parseFloat(galleryItemDefaultPadding, 10) + 5;
  const galleryItemDefaultWidth = galleryContainer.clientWidth - arrowsWidth;

  const isScrolleable =
    galleryContainer.scrollWidth - galleryContainer.clientWidth <= 0
      ? false
      : true;

  if(isScrolleable){
    Array.prototype.map.call(liGalleryItems, (item)=>{item.style.width=`${galleryItemDefaultWidth}px`});
    buttonLeft.disabled = true;
  }

  if (!isScrolleable) {
    buttonRight.classList.add("disabled");
    buttonRight.disabled = true;
    buttonLeft.classList.add("disabled");
    buttonLeft.disabled = true;
  }

  let itemFocused = 0

  buttonRight.onclick = function () {
    itemFocused += 1
    const scrollLeft = (galleryContainer.scrollLeft += galleryItemDefaultWidth);
    buttonLeft.classList.remove("disabled");
    buttonLeft.disabled = false;

    const scrollRight =
      galleryContainer.scrollWidth - galleryContainer.clientWidth;
    if (scrollLeft >= scrollRight) {
      buttonRight.classList.add("disabled");
      buttonRight.disabled = true;
    }
    serviceButtonsArray[itemFocused].onclick();
    serviceButtonsArray[itemFocused].focus();
  };

  buttonLeft.onclick = function () {
    itemFocused -= 1
    const scrollRemaining = (galleryContainer.scrollLeft -=
      galleryItemDefaultWidth);
    buttonRight.classList.remove("disabled");
    buttonRight.disabled = false;
    if (scrollRemaining <= 0) {
      buttonLeft.classList.add("disabled");
      buttonLeft.disabled = true;
    }
    serviceButtonsArray[itemFocused].onclick();
    serviceButtonsArray[itemFocused].focus();
  };
};
