// me traigo lo que necesito del dom
const btn = document.querySelector(".mobile-menu-button");
const sidebar = document.querySelector(".sidebar");
let isSidebarOpen = false;

// agrego el evento listener 
btn.addEventListener("click", () => {
  sidebar.classList.toggle("translate-x-full");
});

// cierro la sidebar si el usuario presiona fuera de ella
document.addEventListener("click", (event) => {
  const isButtonClick = btn === event.target && btn.contains(event.target);
  const isOutsideClick =
    sidebar !== event.target && !sidebar.contains(event.target);

  
  
  if (sidebar.classList.contains("-translate-x-full")) return;

  
  if (isButtonClick) {
    console.log("does not contain");
    sidebar.classList.toggle("-translate-x-full");
    return;
  }

  if (!isButtonClick && isOutsideClick) {
    console.log("outside click");
    sidebar.classList.add("-translate-x-full");
    return;
  }
});
