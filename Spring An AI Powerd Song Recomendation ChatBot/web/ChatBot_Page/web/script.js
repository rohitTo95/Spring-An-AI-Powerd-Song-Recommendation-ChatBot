let user_input = document.getElementById("user_input");

// check machine is connected with internet
let in_status_ball = document.getElementById("in_status_ball");
let in_status_text = document.getElementById("in_status_text");
const internet_checker = () => {
  if (window.navigator.onLine === true) {
    in_status_ball.classList.add("online_ball");
    in_status_text.classList.add("online_text");
  } else {
    in_status_ball.classList.remove("online_ball");
    in_status_text.classList.remove("online_text");
    in_status_ball.classList.add("offline_ball");
    in_status_text.classList.add("offline_text");
    in_status_text.innerText = "Offline";
  }
};
setInterval(internet_checker, 1000);

// header buttons
// powerOff btn

const powerOff = () => {
  if (confirm("Power Off?")) {
    window.close();
  }
};

document.getElementById("powerOff_btn").addEventListener("click", powerOff);

// prompt options
const prompts = document.getElementsByClassName("prompt-options");
Array.from(prompts).forEach((element) => {
  element.addEventListener("click", () => {
    user_input.value = element.innerText;
  });
});

// user input fild area

const sent_btn = document.getElementById("sent_btn");
const sent_query = () => {
  if (user_input.value.length != 0) {
    document.getElementById("prompt_area").style.display = "none";
    // create user message box
    // Get the main container element
    let mainContainer = document.getElementById("chating_area_user_chatBot");
    mainContainer.style.width ="80%"
    mainContainer.style.height ="88vh"
    mainContainer.style.overflowY ="scroll"
    mainContainer.classList.add("auto_margin")
    // Create a new div element
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "chatBox");
    newDiv.setAttribute("id", "chatBox_con");

    // Create the inner HTML structure
    let innerHTML = `
<div class="user_message_area flex flex_direction_c">
<img src="../site-assets/user_image/default.svg" alt=""class="chating_icon">
<div class="user_chatMessage" id="user_chat_message_response">
</div>
</div> 
`;

    // Set the inner HTML of the new div element
    newDiv.innerHTML = innerHTML;
    mainContainer.appendChild(newDiv);
    // Creating p tag
    let pTag = document.createElement("p");
    pTag.textContent = user_input.value;

    // append pTag in bot_chatMessage
    let userChatMessageDiv = newDiv.querySelector(".user_chatMessage");
    userChatMessageDiv.appendChild(pTag);
  }
};


// send user query by pressing enter 
user_input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    console.log("Enter");
    sent_query();
  }
});
sent_btn.addEventListener("click", sent_query);




// take songe number or name after extraction


const song_name_or_number = ()=>{
  let innnerhtml = `
  <div class="chatBox" id="chatBox_con">
  <div class="chatBot_area flex flex_direction_cr" >
      <img src="../site-assets/Mr_Bot.png" alt="" class="chating_icon">
      <div class="bot_chatMessage">
        <p></p>
      </div>
    </div>
  </div>
  `
}


