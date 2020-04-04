const addressInputs = document.querySelectorAll('.address-grid .add-box');
const editAddressBtn = document.querySelector('.address-container .user-headings a');
const showCancelBtns = document.querySelectorAll('.address-container .user-action-buttons button');
editAddressBtn.addEventListener('click',()=>{
if(addressInputs[1].disabled==true)
{
    for(i = 0; i < showCancelBtns.length; i++){
        showCancelBtns[i].classList.toggle('showAddressBtn');
    }
    for (i = 0; i < addressInputs.length; i++) {
    addressInputs[i].classList.toggle('addressInputAdd');
    }
    for (i = 0; i < addressInputs.length; i++) {
        addressInputs[i].disabled=false;
        }
    
    if(editAddressBtn.innerHTML=="Edit"){
        editAddressBtn.innerHTML="Cancel";
    }
    else{
        editAddressBtn.innerHTML="Edit";
    }
}

else{
    for(i = 0; i < showCancelBtns.length; i++){
        showCancelBtns[i].classList.toggle('showAddressBtn');
    }
    for (i = 0; i < addressInputs.length; i++) {
        addressInputs[i].classList.toggle('addressInputAdd');
        }
        for (i = 0; i < addressInputs.length; i++) {
            addressInputs[i].disabled=true;
            }
    
    if(editAddressBtn.innerHTML=="Edit"){
        editAddressBtn.innerHTML="Cancel";
    }
    else{
        editAddressBtn.innerHTML="Edit";
    }
}

});



// CHANGE PASSWORD TOGGLE

const passEdit = document.querySelector('.change-password a');
const showPassOptions = document.querySelector('.input-password');

passEdit.addEventListener('click', ()=>{

showPassOptions.classList.toggle('show-change-password');
if(passEdit.innerHTML=="Edit")
{
    passEdit.innerHTML="Cancel";
}
else{
    passEdit.innerHTML="Edit";
}
});

// USER NAME TOGGLE 

const showNameEdit = document.querySelector('.user-info a');
const firstName= document.getElementById('first-name');
const personalInfoEdit = document.querySelector('.user-headings a');
const lastName = document.getElementById('last-name');
showNameEdit.addEventListener('click',()=>{
    if(firstName.disabled==true )
    {
        firstName.classList.toggle('change-name-field');
        lastName.classList.toggle('change-name-field');
        firstName.disabled= false;
        lastName.disabled=false;

        if(personalInfoEdit.innerHTML=="Edit"){
    personalInfoEdit.innerHTML="Cancel";
}
else{
    personalInfoEdit.innerHTML="Edit";
}
    }
    else{
        firstName.classList.toggle('change-name-field');
        lastName.classList.toggle('change-name-field');
        firstName.disabled= true;
        lastName.disabled=true;
        if(personalInfoEdit.innerHTML=="Edit")
{
    personalInfoEdit.innerHTML="Cancel";
}
else{
    personalInfoEdit.innerHTML="Edit";
}
}
});
