/*
 * Copyright 2019 Google LLC. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/* eslint-disable no-undef, @typescript-eslint/no-unused-vars, no-unused-vars */
import "./style.css";

function initMap(): void {
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      // zoom: 16, //19
      //zoom: 15.3, //19
      zoom: 16.2,
      // center: { lat: 23.79765795047656, lng: 90.42343064752127 },
      // center: { lat: 23.787460477128487, lng: 90.41278673559609 },  
      center: { lat: 23.788718074240638, lng: 90.41289817001395 },
      disableDefaultUI: true, 
      // streetViewControl: false,
      styles: 
      [
        {
          featureType: "landscape.man_made,poi",
          stylers: 
          [
            { visibility: "off" }
          ]
        }
      ]
    }
  );
  
  
  const trafficLayer = new google.maps.TrafficLayer();

  trafficLayer.setMap(map);
}


export { initMap };
