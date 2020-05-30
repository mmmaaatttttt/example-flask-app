$(function () {
  $("#color-ajax-form").on("submit", async function (e) {
    e.preventDefault();
    const color = $("#color").val();
    const response = await axios.post("/colors", { color });
    const { isCool } = response.data;
    $("#colors").append(
      $("<div>")
        .css("background-color", color)
        .text(isCool ? `${color} is so cool!` : `${color}??? UGH LAME.`)
    );
  });
});
