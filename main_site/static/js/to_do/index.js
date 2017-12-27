//Creates a new instance of Vue
new Vue({
    //This binds the vue instance to the element with an ID of todo
    //This also makes all the elements within #todo available to the instance
    el: "#todo",
    //Where we register the values that hold data for the application
    data: {
        newTask: "",
        taskList: []
    },
    //This is where we will hold the methods we want to use in our application
    methods: {
        addTask: function(){
            var task = this.newTask.trim();
            if(task){
                this.taskList.push({
                    text: task,
                    checked: false
                });
            this.newTask = "";
            }
        },

        removeTask: function(task){
            var index = this.taskList.indexOf(task);
            this.taskList.splice(index, 1);
        },

        clearList: function(){
            this.taskList = []
        },

        selectAll: function(){
            var targetValue = this.areAllSelected ? false: true;
            for(var i=0; i < this.taskList.length; i++){
                this.taskList[i].checked = targetValue;
            }
        }
    },

    computed: {
        areAllSelected: function() {
            //Check if every property returns true and if there is at least one to-do item
            return this.taskList.every(function(task){
                return task.checked;
            }) && this.taskList.length > 0;
        }
    }
});