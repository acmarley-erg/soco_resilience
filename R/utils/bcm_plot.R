#' bcm_plot
#'
#' @param bcm_data BCM data
#' @param indicator BCM indicator you want to visualize
#' @param indicator_title Name of the indicator you want to show up
#' @param gcm_type Type of GCM using, added to title
#' @param palette_choice color palette
#' @param pal_dir Either 1 or -1, depending on whether you want to reverse the color palette
#' @param col_limits the limits for the color scale bar
#' @param data_form whether the data is in tidy or wide format
#' 
#'
#' @return facet wrapped bcm plot
#'
#' @examples bcm_plot(bcm_ccsm, bcm_ccsm$cwd, "Climatic Water Deficit", "YlOrRd")

bcm_plot = function(bcm_data, indicator, indicator_title, gcm_type = "", palette_choice, pal_dir = 1, data_form = "wide", col_limits){
  
  
  if (data_form == "tidy"){
   
    bcm_filt <- bcm_data %>% 
      dplyr::filter(climate_variables == indicator)
    
    plot_bcm <- ggplot() +
      geom_sf(data = ca_state, fill = "grey") +
      geom_sf(data = bcm_filt, aes(fill = change_from_hist)) +
      facet_wrap(~wyear_group) +
      scale_fill_distiller(palette = palette_choice, direction = pal_dir) +
      geom_sf(data = soco_bound, color = "green", fill = NA, size = 1, alpha = 0.5) +
      labs(
        title = sprintf("Average %s Change from Historical Baseline (1951-1980) ", indicator_title),
        fill = indicator_title
      ) +
      coord_sf(xlim = c(-124,-122.2), ylim = c(38,38.9)) +
      theme_map() 
    
    
  } else {
    
    plot_bcm <- ggplot() +
      geom_sf(data = ca_state, fill = "grey") +
      geom_sf(data = bcm_data, aes(fill = indicator), color = NA) +
      geom_sf(data = ecoregion, fill = NA, color = "black", size = 1) +
      facet_wrap(~wyear_group) +
      scale_fill_distiller(palette = palette_choice, direction = pal_dir, limits = col_limits) +
      labs(
        title = gcm_type,
        fill = indicator_title
      ) +
      coord_sf(xlim = c(-124,-122.2), ylim = c(38,38.9)) +
      theme_map() +
      theme(legend.position = "bottom", strip.text = element_text(size=11))
    
  }
  
  
  return(plot_bcm)
  
}