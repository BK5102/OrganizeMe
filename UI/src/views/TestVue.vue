<template >
  <div> 
  <!-- <button type="button" class="btn btn-space btn-"> Test </button> -->
    <button @click="count++">
      You clicked me {{ count }} times.
    </button>
  </div>

</template>

<script>
export default {
  data() {
    return {
      count: 0
    }
  }
}
</script>

<style>

</style>