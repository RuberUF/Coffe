function noc(){
  if (registro==="exito"){
    Swal.fire({
  title: "Exito",
  text: "Se registro correctamente :)",
  icon: "succes"
});
  }else if (registro==="error"){
    alert("Error Inesperado");
  }else{
  }
}
noc();
