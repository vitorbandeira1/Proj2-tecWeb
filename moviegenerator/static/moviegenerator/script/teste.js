// const form = document.getElementById("idTeste")
// if (form){
//     form.addEventListener("submit",(event)=>{
//         console.log(event)
//         event.preventDefault()
//     })
// }

window.addEventListener( "load", function () {
    function sendData() {
      const XHR = new XMLHttpRequest();
  
      // Bind the FormData object and the form element
      const FD = new FormData( form );
  
      // Define what happens on successful data submission
      XHR.addEventListener( "load", function(event) {
        alert( event.target.responseText );
      } );
  
    //   // Define what happens in case of error
      XHR.addEventListener( "error", function( event ) {
        alert( 'Oops! Something went wrong.' );
      } );
  
      // Set up our request
      XHR.open( "POST", "/" );
  
      // The data sent is what the user provided in the form
      XHR.send( FD );
    }
  
    // Access the form element...
    const form = document.getElementById( "idTeste" );
  
    // ...and take over its submit event.
    if (form){
        form.addEventListener("submit",(event)=>{
            console.log(event);
            event.preventDefault();

        });
    sendData();
    };