<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/burnish3d/mqtt_chat">
  </a>

<h3 align="center">mqtt_chat</h3>

  <p align="center">
    A command line chat client using the MQTT protocol, written in Python.
    <br />
    <br />
    <a href="https://github.com/burnish3d/mqtt_chat/issues">Report Bug</a>
    ·
    <a href="https://github.com/burnish3d/mqtt_chat/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

mqtt_chat is a light weight command line chat client written in python that uses MQTT to distribute messages and controls the terminal with ANSI control characters.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python3](https://www.python.org/downloads/)
* [PahoMQTT](https://github.com/eclipse/paho.mqtt.python)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Open your terminal
2. Use pip to get the package as
   ```sh
   python3 -m pip install mqtt_chat
   ```
![product-installation]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run as
  ```sh
  python3 -m mqtt_chat -d your_displayname -b mqtt.broker.address -t your/chatroom/topic
  ```
![product-demo]
Exit by hitting ctrl+c

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- Implement obfuscation of plain text
- Bundle a broker app to support setup and use over purely local networks

See the [open issues](https://github.com/burnish3d/mqtt_chat/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact



Project Link: [https://github.com/burnish3d/mqtt_chat](https://github.com/burnish3d/mqtt_chat)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/burnish3d/mqtt_chat.svg?style=for-the-badge
[contributors-url]: https://github.com/burnish3d/mqtt_chat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/burnish3d/mqtt_chat.svg?style=for-the-badge
[forks-url]: https://github.com/burnish3d/mqtt_chat/network/members
[stars-shield]: https://img.shields.io/github/stars/burnish3d/mqtt_chat.svg?style=for-the-badge
[stars-url]: https://github.com/burnish3d/mqtt_chat/stargazers
[issues-shield]: https://img.shields.io/github/issues/burnish3d/mqtt_chat.svg?style=for-the-badge
[issues-url]: https://github.com/burnish3d/mqtt_chat/issues
[license-shield]: https://img.shields.io/github/license/burnish3d/mqtt_chat.svg?style=for-the-badge
[license-url]: https://github.com/burnish3d/mqtt_chat/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/chandlerzach
[product-screenshot]: images/screenshot.png
[product-installation]: images/install_mqtt_chat.gif
[product-demo]: images/demo_mqtt_chat.gif