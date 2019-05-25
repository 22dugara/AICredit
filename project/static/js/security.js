document.addEventListener("DOMContentLoaded", function(event) {
 
  document.getElementById('signout-button').addEventListener('click', function(event) {
    event.preventDefault()
    blockstack.signUserOut("/signin")
  })

  

  if (blockstack.isUserSignedIn() == false) {
    window.location.href= "/signin"
  } 
})