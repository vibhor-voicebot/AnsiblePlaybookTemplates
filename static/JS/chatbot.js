

    window.addEventListener('DOMContentLoaded', function () {

      var container = document.getElementById('chatbot-container');

      function setContainerSize() {
        container.style.width = window.innerWidth + 'px';
        container.style.height = window.innerHeight + 'px';
      }

      setContainerSize();
      window.addEventListener('resize', setContainerSize);
    });

    var chat = document.getElementById("chatbot-chat");
    $(document).ready(function () {

      var chat = document.getElementById("chatbot-chat");


      $("#chatbot-open-container").click(function () {
        $("#open-chat-button").toggle(200);
        $("#close-chat-button").toggle(200);
        $("#chatbot-container").fadeToggle(200);
      });
      //});
      document.getElementById("chatbot-new-message-send-button").addEventListener("click", newInput);

      document.getElementById("chatbot-input").addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          newInput();
        }
      });


      window.addEventListener('DOMContentLoaded', function () {

        var container = document.getElementById('chatbot-container');

        function setContainerSize() {
          container.style.width = window.innerWidth + 'px';
          container.style.height = window.innerHeight + 'px';
        }

        setContainerSize();
        window.addEventListener('resize', setContainerSize);
      });


    });


    function newInput() {
      newText = document.getElementById("chatbot-input").value;
      if (newText != "") {
        document.getElementById("chatbot-input").value = "";
        addMessage("sent", newText);
        generateResponse(newText);
      }
    }


    function addMessage(type, text) {
      var chat = document.getElementById("chatbot-chat");

      var messageDiv = document.createElement("div");
      var responseText = document.createElement("p");
      responseText.appendChild(document.createTextNode(text));

      if (type == "sent") {
        messageDiv.classList.add("chatbot-messages", "chatbot-sent-messages");
      } else if (type == "received") {
        messageDiv.classList.add("chatbot-messages", "chatbot-received-messages");
      }

      messageDiv.appendChild(responseText);
      chat.prepend(messageDiv);
    }




    function generateResponse(prompt) {
      //  var data = "";
      $.get("/get", { msg: prompt }).done(function (data) {
        data = data.replace(/\n/g, "<br>");
        //data = data.replace(/-/g, "<b>**</b>");
        alert(data);
        addMessage("received", data);
      });


      //addMessage("received",  data);
    }


