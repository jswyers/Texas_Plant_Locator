# Texas_Plant_Locator
An update to the  BL Turner Plant Resources Center (University of Texas at Austin) species seach app with improved visualization, easier query interface, and background information. The idea is to make a simple app which directs the user to specific locations to find species of interest and presents any detailed information recorded by the researchers.  Links are provided to the herbarium images for further study.

The herbarium dataset was scraped from the PRC website via Beautiful Soup and Splinter and stored in a Mongo DB. A Leaflet visualization presents query results on a Texas map with detail overlays containing information about date of collection, associated species, collector name, etc.  This allows the user to view the full record and explore the history of the collection. Links are provide for the collected sample images.

The Flask app resides on Heroku.



