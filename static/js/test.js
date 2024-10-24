let formData = {}
const form = document.getElementById('test-form')
const LS = localStorage


form.addEventListener('input', function (event) {
    formData[event.target.name] = event.target.value
    LS.setItem('formData', JSON.stringify(formData))
})

// Восстановление данных
if (LS.getItem('formData')){
    formData = JSON.parse(LS.getItem('formData'))
    console.log(formData)

    for (let key in formData){
        form.elements[key].value = formData[key]
    }
}