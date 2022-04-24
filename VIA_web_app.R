## app.R ##
library(shiny)

ui <- fluidPage(
    titlePanel("Visual Inspection Aide"), hr(style="border-color: blue"),
      fluidRow(
        column(4,
              p("The purpose of this web-based tool is to a provide quick measurement of the level,                stability, and trend of the last seven data points of a condition (e.g., baseline,                   intervention."), p("DIRECTIONS: Enter the value of each data point into the text boxes               to the right and the graphs will update automaticaly."), p("NOTE: Trend will only                    calculate if there are values for 5 or 10 data points.")),
        column(4,
              numericInput("a1", "Data Point 1", value = 3),
              numericInput("a2", "Data Point 2", value = 5),
              numericInput("a3", "Data Point 3", value = 1),
              numericInput("a4", "Data Point 4", value = 9),
              numericInput("a5", "Data Point 5", value = 11)),
        column(4,
              numericInput("a6", "Data Point 6", value = 9),
              numericInput("a7", "Data Point 7", value = 14),
              numericInput("a8", "Data Point 8", value = 7),
              numericInput("a9", "Data Point 9", value = 14),
              numericInput("a10", "Data Point 10", value = 7),
              br())
),
                 
fluidRow(
    column(10, p("Level was calculated using the median of the data and is represented with a dotted green line."),textOutput("med"))),
fluidRow(plotOutput("plot1", height = 500, width = 600), align = "center"), br(),
fluidRow(
        column(10, p("The stability of the data were calculated using the stability envelope. The blue dotted lines on the graph represent the upper and lower limits of the stability envelope."), p("If less than 80% of the data points are within the upper and lower limits, then the data are not stable."), textOutput("Envelope"))),

fluidRow(plotOutput("plot2", height = 500, width = 600), align = "center"), br(),
fluidRow(
         column(10,p("Trend was calculated using the split middle method and is represented by the orange dotted line."))),

fluidRow(plotOutput("plot3", height = 500, width = 600), align = "center"),
fluidRow(plotOutput("plot4", height = 500, width = 600), align = "center"))


                 
                 
server <- function(input, output) { 
    
    
    output$plot1 <- renderPlot({
        data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
        data_max <- max(data, na.rm = TRUE)
        x_axis <- c(1:10)
        mdata <- median(data, na.rm = TRUE)
        plot(x_axis,data, type = "b", ylim = c(0, data_max+2), ylab = "Occurrences", xlab = "Data Points", main = "Level", frame.plot=FALSE)
        axis(1, at = seq(1, 10, by = 1))
        abline(h = mdata, col = "green", lty = "dotted", lwd = 2)
        
    })
    
    output$plot2 <- renderPlot({
        data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
        data_max <- max(data, na.rm = TRUE)
        x_axis <- c(1:10)
        mdata <- median(data, na.rm = TRUE)
        mdata_up <- mdata+(mdata*.1)
        mdata_lo <- mdata-(mdata*.1)
        plot(x_axis,data, type = "b", ylim = c(0, data_max+2), ylab = "Occurrences", xlab = "Data Points", main = "Variability", frame.plot=FALSE)
        axis(1, at = seq(1, 10, by = 1))
        abline(h = mdata_lo, col = "blue", lty = "dotted", lwd = 2)
        abline(h = mdata_up, col = "blue", lty = "dotted", lwd = 2)
    })
        
    output$med <- renderText({
        data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
        mdata <- median(data, na.rm = TRUE)
        paste("The median is", mdata)
    })
    
    
     output$Envelope <- renderText({
            data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
            mdata <- median(data, na.rm = TRUE)
            mdata_up <- mdata+(mdata*.1)
            mdata_lo <- mdata-(mdata*.1)
            sta_env <- sum(data <= mdata_up & data >= mdata_lo)
            #Percent of Data Points in Stability Envelope
            results <- (sta_env/length(data[!is.na(data)]))*100
            results[is.na(results)] = 0
            
            paste("The percent of data points within the stability envelope is", results)
    })
    
     output$plot3 <- renderPlot({
     data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
     data_max <- max(data, na.rm = TRUE)
     a_data <- data[c(1:5)]
     x <- c(1:5)
     sub_data1 <- a_data[c(1:2)]
     sub_data2 <- a_data[c(4:5)]
     med_sub_data1 <- median(sub_data1)
     med_sub_data2 <- median(sub_data2)
     plot(x,a_data, type = "b", ylim = c(0, data_max+2), ylab = "Occurrences", xlab = "Data Points", main = "Trend: Data Points 1-5", frame.plot = FALSE)
     segments(x0 = 1.5, y0 = med_sub_data1, x1 = 4.5, y1 = med_sub_data2, col = "orange", lty = "dotted", lwd = 2)
     })
     
     output$plot4 <- renderPlot({
         data <- c(input$a1, input$a2, input$a3, input$a4, input$a5, input$a6, input$a7, input$a8, input$a9, input$a10)
         data_max <- max(data, na.rm = TRUE)
         x <- c(1:10)
         sub_data1 <- data[c(1:5)]
         sub_data2 <- data[c(6:10)]
         med_sub_data1 <- median(sub_data1)
         med_sub_data2 <- median(sub_data2)
         plot(x,data, type = "b", ylim = c(0, data_max+2), ylab = "Occurrences", xlab = "Data Points", main = "Trend: Data Points 1-10", frame.plot = FALSE)
         axis(1, at = seq(1, 10, by = 1))
         segments(x0 = 3, y0 = med_sub_data1, x1 = 8, y1 = med_sub_data2, col = "orange", lty = "dotted", lwd = 2)
     })
     
}

shinyApp(ui, server)