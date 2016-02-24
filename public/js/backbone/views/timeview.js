App.Views.TimeView = Backbone.View.extend({
  el: '#content',

  initialize: function(){
    $('#content').empty();
    this.vizTemplate = Handlebars.compile($('#viz-template').html());
    this.render();
    this.listenTo(this.collection, 'sync', this.render)
  },

  render: function(){
    this.$el.append(this.vizTemplate({title: "Timeline of Travels"}))
    var allTrips = this.collection;
    var sortedTrips=allTrips.sortBy(function(model){
      return start = new Date(model.get('start_date'))
    })
    _.each(sortedTrips, function(trip){

    })

    var testData = [
    {label: "person a", times: [
      {"starting_time": 1355752800000, "ending_time": 1355759900000},
      {"starting_time": 1355767900000, "ending_time": 1355774400000}]},
    {label: "person b", times: [
      {"starting_time": 1355759910000, "ending_time": 1355761900000}]},
    {label: "person c", times: [
      {"starting_time": 1355761910000, "ending_time": 1355763910000}]},
    ];

    var chart = d3.timeline();

    var svg = d3.select(".chart").append("svg").attr("width", 500).datum(testData).call(chart);
    }
})
