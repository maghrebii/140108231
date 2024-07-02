document.addEventListener("DOMContentLoaded",()=>{
        
         const usercontainer = document.getElementById("user_cotainer");
         async function fetchusers() {
            const res = await fetch("https://reqres.in/api/users/");
            const json = await res.json();
            //console.log(json.data)
            displayUsers(json.data);
         }

function displayUsers(users){

    users.forEach(user => {

        const userDiv = document.createElement("div")

        const userName = document.createElement("p")
        userName.innerHTML = `<strong>${user.first_name}</strong>`;
        userDiv.appendChild(userName);


        
        const userEmail = document.createElement("p")
        userEmail.innerHTML = `<strong>${user.email}</strong>`;
        userDiv.appendChild(userEmail);

        const userAvatar = document.createElement("img");
        userAvatar.src = user.avatar
        
        userName.innerHTML = `<strong>${user.avatar}</strong>`;
        userDiv.appendChild(userAvatar);


        usercontainer.appendChild(userDiv)


})
}

fetchusers();



});



/* <div>
    <p>
        first_name
    </p>

    <p>
        eamil
    </p>

    <img src=""/>

   
</div> */