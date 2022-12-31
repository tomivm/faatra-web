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
  const galleryItemDefault = document.getElementsByClassName("blue-bg-item")[0];

  const galleryItemDefaultPadding = window
    .getComputedStyle(galleryItemDefault, null)
    .getPropertyValue("padding");

  const galleryItemDefaultWidth =
    galleryItemDefault.clientWidth + parseInt(galleryItemDefaultPadding, 10);
  console.log("galleryItemDefaultWidth", galleryItemDefaultPadding);

  const isScrolleable =
    galleryContainer.scrollWidth - galleryContainer.clientWidth <= 0
      ? false
      : true;

  if (!isScrolleable) {
    buttonRight.classList.add("disabled");
    buttonLeft.classList.add("disabled");
  }

  buttonRight.onclick = function () {
    const scrollLeft = (galleryContainer.scrollLeft += galleryItemDefaultWidth);
    buttonLeft.classList.remove("disabled");

    const scrollRight =
      galleryContainer.scrollWidth - galleryContainer.clientWidth;
    if (scrollLeft >= scrollRight) {
      buttonRight.classList.add("disabled");
    }
  };

  buttonLeft.onclick = function () {
    const scrollRemaining = (galleryContainer.scrollLeft -=
      galleryItemDefaultWidth);
    buttonRight.classList.remove("disabled");
    if (scrollRemaining <= 0) {
      buttonLeft.classList.add("disabled");
    }
  };
};
