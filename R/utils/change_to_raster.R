#' change_to_raster
#' 
#' function to turn polygons into rasters
#'
#' @param chosen_polygon the polygon to change into a raster
#' @param empty_raster empty raster 
#' @param rank either a number if it's a binary polygon or which field to use when turning into a raster
#'
#' @return
#' @export
#'
#' @examples

change_to_raster = function(chosen_polygon, empty_raster, rank){
  
  polygon_crs <- sf::st_transform(chosen_polygon, st_crs(empty_raster))
  
  final_raster <- fasterize::fasterize(sf = polygon_crs, raster = empty_raster, field = rank, background = 0)
  
  return(final_raster)
  
}
