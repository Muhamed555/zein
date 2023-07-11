<div align="center">
  <img src="logo.png" alt="Ather logo" width="400" height="auto" />
<hr>
  <p> A Python package to set restrictions on visual content of all kinds and protect users from seeing harmful content, and ensure the safety of input and output machine learning models.</p>
</div>

**Contents**

  * [Library Mission](#Library-Mission)
  * [Installation](#Installation)
  * [Sample Code](#Sample-Code)
  * [Try the package on Colab](#Try-the-package-on-Colab)
  * [Call for Contributions](#Call-for-Contributions)
  * [License](#license)
    
# Package Mission
- The package includes an Arabic script swear word filter module, using a comprehensive list of swear words and an intelligent content detection algorithm
- The package includes features for detecting sexual requests from users of machine learning models, such as requests that include creating images that contain sexual content.
- The package includes features that can detect and evaluate images out of 100 to see if they contain sexual content or not, and some other helpful features.
  
## Installation

    pip install zein

## Sample Code

    from zein.text import ArabicFilter
  
    af = ArabicFilter()
    
    text = "انت انسان ابن كلب"
    af.censor(text)

    // انت انسان ابن ***
    
    af.find_insulting_words(text)
    // [(4, كلب)]
    
    af.is_profane(text)
    // True
## Try The package on Colab


## Call for Contributions
<p>We Need Your Help The zein project values your skills and passion!</p>
<p>We appreciate any small enhancements or fixes you can make. If you want to make bigger changes to the source code, please let us know through the mailing list first.</p>

There are many other ways to contribute to NumPy besides writing code. You can also:
- Help us manage new and old issues
- Create tutorials, presentations, and other learning materials
- Evaluate pull requests





