App.Views.TimeView = Backbone.View.extend({
  el: '#content',

  initialize: function(){
    $('#content').empty();
    this.vizTemplate = Handlebars.compile($('#viz-template').html());
    this.render();
    this.listenTo(this.collection, 'sync', this.render)
  },

  render: function(){

    var allTrips = this.collection;
    var sortedTrips=allTrips.sortBy(function(model){
      return start = new Date(model.get('start_date'))
    })
    _.each(sortedTrips, function(trip){

    })

  }
})
