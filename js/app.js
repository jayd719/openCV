// Create and append dynamic styles
function createDynamicStyles() {
  const styleElement = document.createElement("style");
  styleElement.textContent = `
  #creation-time{
  margin-top: 100px;
  }
    h2 {
        font-size: 24px;
        margin-bottom: 20px;
        text-transform: capitalize;

    }
    .image-grid {
        display: grid;
        border: solid 1px #d3d3d3;
    }
    .image-item {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .image-item figcaption {
        margin-top: 8px;
        font-size: 12px;
        color: #666;
        text-align: center;
    }
    .controls {
        position: fixed;
        top: 20px;
        left: 20px;
        right: 20px;
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 8px 20px rgba(8, 7, 7, 0.1);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .control-group {
        display: flex;
        align-items: center;
    }
    .control-group label {
        margin-right: 10px;
    }
    input[type="range"] {
        width: 300px;
    }
  `;
  document.head.appendChild(styleElement);
}

// Apply styles to the elements
function applyStyles() {
  const resultsSection = document.getElementById("resultssection");

  if (!resultsSection) return;
  resultsSection.style.display="flex"
  // Apply grid layout to the results section
  resultsSection.classList.add("image-grid");

  // Update div elements to have the "image-item" class
  resultsSection.querySelectorAll("div").forEach((div) => {
    div.classList.add("image-item");

    // Update figcaption inside div
    div.querySelectorAll("figcaption").forEach((figcaption) => {
      figcaption.classList.add("image-caption");
    });
  });
}

// Update dimensions of all images dynamically
function updateImages(size) {
  document.querySelectorAll("img").forEach((img) => {
    img.style.width = `${size}px`;
    img.style.height = `${size}px`;
  });
}

// Render a slider to control image sizes
function renderSlider() {
  const container = document.createElement("div");
  container.className = "controls";

  const controlGroup = document.createElement("div");
  controlGroup.className = "control-group";

  const label = document.createElement("label");
  label.textContent = "Image Size:";

  const slider = document.createElement("input");
  slider.type = "range";
  slider.id = "slider";
  slider.min = "50";
  slider.max = "500";
  slider.step = "25";
  slider.value = "200";

  controlGroup.appendChild(label);
  controlGroup.appendChild(slider);
  container.appendChild(controlGroup);
  document.body.appendChild(container);

  // Update images on slider input
  slider.addEventListener("input", (event) => {
    updateImages(event.target.value);
  });
}


// Initialize the application
function initialize() {
  createDynamicStyles(); // Add styles dynamically
  applyStyles(); // Apply classes and structure
  updateImages(200); // Initial image size
  renderSlider(); // Render the slider for image resizing

  // Update the time every second
  const startTime = new Date(document.getElementById("creation-time").innerText)
  setInterval(() => updateTime(startTime), 1000);
  updateTime(startTime);
}

// Call the initialize function to start the app
initialize();


// Update and display the time elapsed since a given start time
function updateTime(startTime) {
  const timeElement = document.getElementById("creation-time");
  
  if (!timeElement) return;

  // Get the current time
  const now = new Date();

  // Calculate the time difference in milliseconds
  const timeDifference = now - startTime;

  // Convert milliseconds to hours, minutes, and seconds
  const hours = Math.floor(timeDifference / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  // Format the time elapsed string
  const timeString = `${hours}h ${minutes}m ${seconds}s`;

  // Update the content of the element
  timeElement.textContent = `Created: ${timeString} Ago`;
}


