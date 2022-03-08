const servicesArrayMock = [
  {
    id: 0,
    servicio: "Asesoria",
    descripcion:
      "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minus amet labore illum repellendus nemo et, soluta doloremque repudiandae, veniam omnis maiores quo deserunt magni odit tenetur facere, iste harum officia administracion@faatra.org.ar. Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
    encargados: [
      {
        cargo: "Asesor Paritaria",
        nombre: "DR. MARTÍN BRUNENGO",
        fotoSrc: "./../images/mananger-pic.jpeg",
      },
      {
        cargo: "Asesor contable",
        nombre: "BENGOECHEA BRACCO Y ASOCIADOS",
        fotoSrc: "./../images/mananger-pic.jpeg",
      },
    ],
  },
  {
    id: 1,
    servicio: "Costo hora",
    descripcion:
      "Lorem,Costo hora ipsum dolor sit amet consectetur adipisicing elit. Minus amet labore illum repellendus nemo et, soluta doloremque repudiandae, veniam omnis maiores quo deserunt magni odit tenetur facere, iste harum officia administracion@faatra.org.ar. Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
    encargados: [
      {
        cargo: "Asesor Paritaria",
        nombre: "DR. MARTÍN BRUNENGO",
        fotoSrc: "./../images/mananger-pic.jpeg",
      },
    ],
  },
  {
    id: 2,
    servicio: "Convenios",
    descripcion:
      "Lorem, Convenios ipsum dolor sit amet consectetur adipisicing elit. Minus amet labore illum repellendus nemo et, soluta doloremque repudiandae, veniam omnis maiores quo deserunt magni odit tenetur facere, iste harum officia administracion@faatra.org.ar. Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
    encargados: [
      {
        cargo: "Asesor Paritaria",
        nombre: "DR. MARTÍN BRUNENGO",
        fotoSrc: "./../images/mananger-pic.jpeg",
      },
    ],
  },
  {
    id: 3,
    servicio: "Escalas",
    descripcion:
      "Lorem, Escalas dolor sit amet consectetur adipisicing elit. Minus amet labore illum repellendus nemo et, soluta doloremque repudiandae, veniam omnis maiores quo deserunt magni odit tenetur facere, iste harum officia administracion@faatra.org.ar. Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
    encargados: [
      {
        cargo: "Asesor Paritaria",
        nombre: "DR. MARTÍN BRUNENGO",
        fotoSrc: "./../images/mananger-pic.jpeg",
      },
    ],
  },
];

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

  const descriptionTextNode = document.createTextNode(
    servicesArrayMock[id].descripcion
  );
  description.innerHTML = "";
  description.appendChild(descriptionTextNode);

  manangersContainer.innerHTML = "";
  servicesArrayMock[id].encargados.map((encargado) => {
    console.log("map");
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
  element.scrollIntoView();
  // scrollToContent();
}

function init() {
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
