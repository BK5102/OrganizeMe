console.log("Hello Vue")
const app = Vue.createApp({
    //template: '<h2>Another template </h2>'
    data() {
        return {
            showBooks: true,
            books: [
                {title: "Harry Potter Chamber of Secrets", author: "JK Rowling", isFav: true},
                {title: "Percy Jackson", author: "Rick Riordan", isFav: false}
            ]
        }
    },

    methods: {
        toggleShowBooks(){
            this.showBooks = !this.showBooks
        },

        handleEvent(e,num){
            console.log(e, e.type)
            if (num){
                console.log(num)
            }
        },
/*
        handleMouseMove(e){
            this.x = e.offsetX
            this.y = e.offsetY
        }
*/


    }


})

app.mount("#app")