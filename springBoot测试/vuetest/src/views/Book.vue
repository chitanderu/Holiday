<template>
    <div>
        <table>
            <tr>
                <td> name</td>
                <td>  id  </td>
                <td>   author   </td>
            </tr>
            <tr v-for="items in books ">

                <td> {{items.id}}}</td>
                <td> {{items.name}}}</td>
                <td> {{items.author}}}</td>

            </tr>
        </table>
        {{msg}}}
    </div>
</template>

<script>
    export default {
        name: "Book" ,
        data(){
            return{
                msg:'hello',
                         books:[
                             {
                                   id: 1,
                                   name: "soap",
                                  author: "long yuan"
                             }


                         ]



            }
        }
    }
</script>

<style scoped>

</style>