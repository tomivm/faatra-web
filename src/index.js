function openMenu() {
  const addOpenClass = () => {
    const navbarContainer = document.getElementById("navbar-container");
    console.log(navbarContainer.classList);

    if (navbarContainer.classList.contains("navbar-container-open"))
      return navbarContainer.classList.remove("navbar-container-open");
    return navbarContainer.classList.add("navbar-container-open");
  };
  console.log("openMenu");
  addOpenClass();

  const navbarItems = document.getElementsByClassName("navbar-item");
  const navbarItemsArray = Array.prototype.slice.call(navbarItems);
  navbarItemsArray.forEach((item) => {
    console.log(item.style.display);
    if (item.style.display !== "block") return (item.style.display = "block");
    return (item.style.display = "none");
  });
}
