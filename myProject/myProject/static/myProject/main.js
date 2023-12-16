function createTask(){
    const postData = {task: document.getElementById("inputTextbox").value}
    const requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(postData),
    }

    fetch('http://127.0.0.1:8080/api/todo', requestOptions)
    .then(response =>{
        if(!response.ok){
            throw new Error('Erro na requisição: ${response.status}')
        }
        return response.json()
    })
    location.reload()
}

function deleteTask(id){
    const requestOptions = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    }
    fetch(`http://127.0.0.1:8080/api/todo/${id}`, requestOptions)
    .then(response =>{
        if(!response.ok){
            throw new Error('Erro na requisição: ${response.status}')
        }
    })
    location.reload()
}