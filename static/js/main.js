const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e)=>{
            if(!confirm('ATENCION!!! ESTA SEGURO DE ELIMINAR ESTE CONTACTO')){
                e.preventDefault();
            }
        });
    });
}