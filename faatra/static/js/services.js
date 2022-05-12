window.onload = init;

const renderServiceContent = (id = 0) => {
  if (!document.getElementById("service-full")) return;
  const tittle = document.getElementById("service-tittle");
  const description = document.getElementById("service-description");
  const manangersContainer = document.getElementById("service-manangers");

  const tittleTextNode = document.createTextNode(
    servicesArrayMock[id].servicio
  );
  tittle.innerHTML = "";
  tittle.appendChild(tittleTextNode);

  const str = servicesArrayMock[id].descripcion;
  description.innerHTML = "";
  description.insertAdjacentHTML("beforeend", str);

  manangersContainer.innerHTML = "";
  servicesArrayMock[id].encargados.map((encargado) => {
    const manangerItem = document.createElement("div");
    manangerItem.classList.add("service-mananger");

    const manangerPic = document.createElement("img");
    manangerPic.src = encargado.fotoSrc;
    manangerPic.classList.add("mananger-pic");

    const position = document.createElement("p");
    const positionTextNode = document.createTextNode(encargado.cargo);
    position.appendChild(positionTextNode);

    const name = document.createElement("p");
    const nameTextNode = document.createTextNode(encargado.nombre);
    name.appendChild(nameTextNode);

    manangerItem.appendChild(manangerPic);
    manangerItem.appendChild(position);
    manangerItem.appendChild(name);

    manangersContainer.appendChild(manangerItem);
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
  renderServiceContent(0);
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
