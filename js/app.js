
document.querySelectorAll("div").forEach(element => {
console.log(element)
  element.style.border="solid 1px lightgray"
  element.style.marginTop="50px"

  element.querySelectorAll("figcaption").forEach(l =>{
    l.style.fontSize="x-small"
  })
});


document.body.style.display="flex"





function updateImages(w){
  document.querySelectorAll("img").forEach(element =>{
    element.style.height = `${w}px`
    element.style.width = `${w}px`
})
}

updateImages(200)

// Function to render the slider
function renderSlider() {
    // Create the input element
    const slider = document.createElement("input");

    // Set attributes for the slider
    slider.type = "range";
    slider.id = "slider";
    slider.min = "50";
    slider.max = "500";
    slider.step = "25";
    slider.value = "200";

    // Append the slider to the container
    const container = document.createElement("div");
    container.style.position = "fixed";
    container.style.zIndex=100

    document.body.appendChild(container)
    container.appendChild(slider);

    // Log the slider value on input change
    slider.addEventListener("input", (event) => {
      
      updateImages(event.target.value)
      
      
    });
  }

  // Call the function to render the slider
  renderSlider();

  /**
 * Dynamically updates CSS properties of an element or elements.
 * @param {string} selector - The CSS selector of the target element(s).
 * @param {string} property - The CSS property to update (e.g., 'backgroundColor', 'color').
 * @param {string} value - The new value for the CSS property.
 */
function updateCSS(selector, value) {
  // Select all matching elements
  const elements = document.querySelectorAll(selector);
  
  // Loop through all selected elements and apply the CSS property
  elements.forEach(element => {
      element.className=value
  });
}

// Change the background color of all figure captions
updateCSS('figcaption', "text-sm text-gray-600 pb-10 scale-[.75");

// Change the border of all images
updateCSS('img', '2px solid #ff0000');

// Change font size of section titles
updateCSS('h3', '24px');
