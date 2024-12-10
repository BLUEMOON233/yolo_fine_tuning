#include <iostream>

#include <string>
#include <vector>
#include "assert.h"
#include <time.h>
#include "opencv2/core/core.hpp"
#include "opencv2/core/types.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace std;

class PascalLabels {
public:
    PascalLabels() {
        for(int i = 0 ; i < 80; i ++) {
            string x = "NA";
            mLabels.push_back( x );
        }

        mLabels[0]  = "aeroplane";
        mLabels[1]  = "bicycle";
        mLabels[2]  = "bird";
        mLabels[3]  = "boat";
        mLabels[4]  = "bottle";
        mLabels[5]  = "bus";
        mLabels[6]  = "car";
        mLabels[7]  = "cat";
        mLabels[8]  = "chair";
        mLabels[9]  = "cow";
        mLabels[10] = "diningtable";
        mLabels[11] = "dog";
        mLabels[12] = "horse";
        mLabels[13] = "motorbike";
        mLabels[14] = "person";
        mLabels[15] = "pottedplant";
        mLabels[16] = "sheep";
        mLabels[17] = "sofa";
        mLabels[18] = "train";
        mLabels[19] = "tvmonitor";
    }

    string pascal_get_label(int i) {
        assert( i >= 0 && i < 20 );
        return mLabels[i];
    }

    cv::Scalar pascal_get_color(int i) {
        float r;
        srand(i);
        r = (float)rand() / RAND_MAX;
        int red    = int(r * 255);

        srand(i + 1);
        r = (float)rand() / RAND_MAX;
        int green    = int(r * 255);

        srand(i + 2);
        r = (float)rand() / RAND_MAX;
        int blue    = int(r * 255);

        return cv::Scalar(blue, green, red);
    }

    cv::Scalar get_inverse_color(cv::Scalar color) {
        int blue = 255 - color[0];
        int green = 255 - color[1];
        int red = 255 - color[2];
        return cv::Scalar(blue, green, red);
    }


private:
  vector<string> mLabels;

};
