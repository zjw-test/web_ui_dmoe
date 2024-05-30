FROM xxxx
RUN rm -rf /export/*
RUN mkdir -p /export/web-ui-test
COPY . /export/web-ui-test
WORKDIR /export/web-ui-test
CMD ["/bin/bash"]